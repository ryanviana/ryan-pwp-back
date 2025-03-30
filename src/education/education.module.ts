import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';
import { EducationService } from './education.service';
import { EducationController } from './education.controller';
import { Education, EducationSchema } from './entities/education.entity';

@Module({
  imports: [
    MongooseModule.forFeature([
      { name: Education.name, schema: EducationSchema },
    ]),
  ],
  controllers: [EducationController],
  providers: [EducationService],
})
export class EducationModule {}
