import { IsString, IsArray, IsNotEmpty } from 'class-validator';

export class CreateSkillCategoryDto {
  @IsString()
  @IsNotEmpty()
  name: string;

  @IsArray()
  @IsString({ each: true })
  @IsNotEmpty()
  skills: string[];
}
